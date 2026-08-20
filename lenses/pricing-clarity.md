# Pricing clarity lens

Whether the user can tell what they are about to pay and what they are paying
with. Runs on carts, checkouts, payment pickers, subscriptions, and paywalls.

## Look for

- **The unreadable total.** The final amount clipped, truncated, below the
  fold, or rendered smaller than the line items that add up to it.
- **Fees that appear late.** Service fees, delivery fees, or taxes introduced
  at the last step rather than carried forward.
- **The unidentified instrument.** A selected payment method with no last four
  digits, no expiry, and no brand, especially when the unselected options in
  the same list show all three.
- **Unpriced commitment.** A subscribe or start-trial CTA with no amount, no
  renewal date, and no cancellation terms in view.
- **Ambiguous free.** "Free" next to a line item without saying free until
  when, or free because of what.
- **Currency drift.** A missing or inconsistent currency symbol across rows.

## Ignore

Whether the price is a good deal, the pricing strategy, and any figure you
cannot see on screen.

## Severity

Rank by whether the user could be charged an amount they did not read or
charged on an instrument they did not identify. Both are refund and chargeback
territory, so they outrank presentation issues.

## Phrasing

Contrast the offending row against its siblings when the siblings get it right.
That comparison is the argument.

```bash
revyl atlas annotations create --app "$APP" --observation "$OBS" \
  --target "the Personal card row with the filled radio button, below SprintCash balance" \
  --body "This is the selected payment method and the only row with no identifying detail. Visa shows last four and expiry, Mastercard shows last four and expiry. The user cannot confirm what they are about to be charged on."
```
