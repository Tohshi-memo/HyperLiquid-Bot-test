# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T23:37:31.370121+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1233` n `12`; crypto_alt avg `0.0348` n `228`; crypto_major avg `0.1102` n `8`; equity avg `0.0804` n `74`; fx avg `-0.0183` n `6`; index avg `-0.0596` n `23`; metal avg `-0.0043` n `18`; unknown avg `0.0165` n `556`
- 1h: commodity avg `0.022` n `12`; crypto_alt avg `-0.1709` n `228`; crypto_major avg `0.0225` n `8`; equity avg `0.0941` n `74`; fx avg `-0.0393` n `6`; index avg `-0.0585` n `23`; metal avg `0.1245` n `18`; unknown avg `-0.0258` n `556`
- 4h: commodity avg `-0.334` n `12`; crypto_alt avg `-0.2542` n `228`; crypto_major avg `-0.3995` n `8`; equity avg `0.3696` n `74`; fx avg `0.0256` n `6`; index avg `0.211` n `23`; metal avg `0.0135` n `18`; unknown avg `-0.3927` n `556`
- 24h: commodity avg `-2.9262` n `12`; crypto_alt avg `4.2118` n `228`; crypto_major avg `4.2638` n `8`; equity avg `5.029` n `74`; fx avg `0.0908` n `6`; index avg `2.7119` n `23`; metal avg `4.0961` n `18`; unknown avg `2.4874` n `530`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1455`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
