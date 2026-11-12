# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T23:37:31.172441+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0029` n `13`; crypto_alt avg `0.0181` n `239`; crypto_major avg `0.0364` n `8`; equity avg `0.2002` n `162`; fx avg `0.0005` n `6`; index avg `0.0209` n `27`; metal avg `0.0247` n `20`; unknown avg `0.0366` n `1261`
- 1h: commodity avg `-0.0153` n `13`; crypto_alt avg `0.1775` n `239`; crypto_major avg `0.2645` n `8`; equity avg `0.5777` n `162`; fx avg `0.0087` n `6`; index avg `0.0716` n `27`; metal avg `0.0363` n `20`; unknown avg `83.1301` n `1227`
- 4h: commodity avg `0.0298` n `13`; crypto_alt avg `0.7358` n `239`; crypto_major avg `0.4469` n `8`; equity avg `0.7977` n `162`; fx avg `-0.005` n `6`; index avg `0.0951` n `27`; metal avg `0.0233` n `20`; unknown avg `0.8057` n `1187`
- 24h: commodity avg `0.9099` n `13`; crypto_alt avg `-0.5735` n `239`; crypto_major avg `-1.5308` n `8`; equity avg `-0.4203` n `162`; fx avg `-0.1215` n `6`; index avg `0.038` n `27`; metal avg `-0.5847` n `20`; unknown avg `51.4204` n `1121`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1298`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
