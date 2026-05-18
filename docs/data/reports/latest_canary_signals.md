# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T20:22:16.737514+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1094` n `12`; crypto_alt avg `0.0584` n `228`; crypto_major avg `0.0201` n `8`; equity avg `0.0205` n `66`; fx avg `0.0161` n `6`; index avg `0.0201` n `23`; metal avg `0.0972` n `18`; unknown avg `0.0689` n `383`
- 1h: commodity avg `-0.2385` n `12`; crypto_alt avg `0.7851` n `228`; crypto_major avg `0.7565` n `8`; equity avg `0.5233` n `66`; fx avg `0.0174` n `6`; index avg `0.3227` n `23`; metal avg `0.2477` n `18`; unknown avg `0.3315` n `383`
- 4h: commodity avg `-0.4629` n `12`; crypto_alt avg `0.9767` n `228`; crypto_major avg `1.0506` n `8`; equity avg `-0.0403` n `66`; fx avg `-0.007` n `6`; index avg `0.0268` n `23`; metal avg `0.3933` n `18`; unknown avg `0.4549` n `383`
- 24h: commodity avg `0.4976` n `12`; crypto_alt avg `-1.6668` n `228`; crypto_major avg `-1.852` n `8`; equity avg `-0.9543` n `66`; fx avg `0.1866` n `6`; index avg `-0.4131` n `23`; metal avg `1.0539` n `18`; unknown avg `-0.0253` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1621`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1594`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1539`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
