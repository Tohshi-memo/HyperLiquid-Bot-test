# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T08:07:16.644987+00:00`
- Correlation status: `ready`
- Asset price records: `532`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.33` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `2.2164` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.1034` n `12`; crypto_alt avg `0.0795` n `228`; crypto_major avg `-0.011` n `8`; equity avg `0.0519` n `65`; fx avg `0.0059` n `4`; index avg `0.0371` n `23`; metal avg `0.1143` n `18`; unknown avg `0.2286` n `358`
- 1h: commodity avg `-0.0375` n `12`; crypto_alt avg `0.2317` n `228`; crypto_major avg `0.3582` n `8`; equity avg `0.1836` n `65`; fx avg `0.0315` n `4`; index avg `0.108` n `23`; metal avg `0.4606` n `18`; unknown avg `0.3749` n `358`
- 4h: commodity avg `-0.87` n `12`; crypto_alt avg `2.2942` n `228`; crypto_major avg `1.3464` n `8`; equity avg `0.7571` n `65`; fx avg `-0.0966` n `4`; index avg `0.3044` n `23`; metal avg `1.3827` n `18`; unknown avg `0.7112` n `356`
- 24h: commodity avg `-1.9412` n `7`; crypto_alt avg `1.476` n `223`; crypto_major avg `-0.3352` n `7`; equity avg `1.7984` n `47`; fx avg `0.0112` n `4`; index avg `1.6769` n `6`; metal avg `2.2439` n `7`; unknown avg `1.2745` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.132`, n `528`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1244`, n `528`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1051`, n `524`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1018`, n `528`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0942`, n `524`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0839`, n `524`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0829`, n `524`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0782`, n `524`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.072`, n `524`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0639`, n `528`, weak_sample_signal
