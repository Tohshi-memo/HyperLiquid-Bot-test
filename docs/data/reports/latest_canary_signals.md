# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T17:30:24.108327+00:00`
- Correlation status: `ready`
- Asset price records: `284`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1949` n `7`; crypto_alt avg `0.1456` n `223`; crypto_major avg `0.0441` n `7`; equity avg `0.186` n `42`; fx avg `0.0033` n `4`; index avg `0.0146` n `9`; metal avg `0.0188` n `7`; unknown avg `0.0042` n `314`
- 1h: commodity avg `-0.1852` n `7`; crypto_alt avg `0.4737` n `223`; crypto_major avg `0.4161` n `7`; equity avg `0.0536` n `42`; fx avg `0.0014` n `4`; index avg `0.144` n `9`; metal avg `0.2514` n `7`; unknown avg `0.0023` n `314`
- 4h: commodity avg `0.911` n `7`; crypto_alt avg `0.9249` n `223`; crypto_major avg `0.9339` n `7`; equity avg `-0.3938` n `42`; fx avg `-0.0092` n `4`; index avg `0.2807` n `9`; metal avg `-0.4577` n `7`; unknown avg `-0.4784` n `314`
- 24h: commodity avg `2.0704` n `7`; crypto_alt avg `2.0076` n `223`; crypto_major avg `1.4046` n `7`; equity avg `-0.0857` n `42`; fx avg `-0.0833` n `4`; index avg `0.6633` n `9`; metal avg `-2.2304` n `7`; unknown avg `-0.8496` n `312`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2397`, n `280`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2341`, n `280`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1658`, n `276`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1646`, n `276`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1548`, n `276`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1541`, n `276`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1522`, n `280`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1495`, n `280`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1443`, n `280`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1397`, n `276`, weak_sample_signal
