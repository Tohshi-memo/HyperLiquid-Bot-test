# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T09:58:44.829658+00:00`
- Correlation status: `ready`
- Asset price records: `635`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.0` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.3315` n `12`; crypto_alt avg `-0.0638` n `228`; crypto_major avg `-0.0788` n `8`; equity avg `-0.2375` n `65`; fx avg `0.031` n `5`; index avg `-0.0058` n `23`; metal avg `-0.1404` n `18`; unknown avg `-0.0349` n `375`
- 1h: commodity avg `0.2696` n `12`; crypto_alt avg `0.0321` n `228`; crypto_major avg `-0.0076` n `8`; equity avg `-0.1339` n `65`; fx avg `0.0238` n `5`; index avg `0.0135` n `23`; metal avg `-0.114` n `18`; unknown avg `-0.0281` n `375`
- 4h: commodity avg `0.1725` n `12`; crypto_alt avg `0.3131` n `228`; crypto_major avg `0.2491` n `8`; equity avg `0.6308` n `65`; fx avg `0.0814` n `5`; index avg `0.1882` n `23`; metal avg `-0.162` n `18`; unknown avg `0.3831` n `355`
- 24h: commodity avg `1.3818` n `12`; crypto_alt avg `1.1324` n `228`; crypto_major avg `-1.4455` n `8`; equity avg `-0.935` n `65`; fx avg `0.2568` n `5`; index avg `-0.4025` n `23`; metal avg `-0.6577` n `18`; unknown avg `-0.2637` n `355`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1375`, n `627`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1365`, n `627`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1131`, n `631`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.098`, n `631`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0959`, n `631`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0948`, n `631`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0874`, n `627`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0866`, n `627`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0762`, n `631`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0751`, n `631`, weak_sample_signal
