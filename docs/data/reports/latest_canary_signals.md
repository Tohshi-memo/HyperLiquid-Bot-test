# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T11:07:30.244214+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0196` n `12`; crypto_alt avg `-0.0311` n `229`; crypto_major avg `-0.0533` n `8`; equity avg `0.2317` n `91`; fx avg `0.0116` n `6`; index avg `0.0125` n `25`; metal avg `-0.023` n `20`; unknown avg `-0.0243` n `766`
- 1h: commodity avg `0.0376` n `12`; crypto_alt avg `0.1696` n `229`; crypto_major avg `0.0651` n `8`; equity avg `0.3325` n `91`; fx avg `0.0238` n `6`; index avg `0.0355` n `25`; metal avg `-0.0241` n `20`; unknown avg `0.0956` n `766`
- 4h: commodity avg `0.0262` n `12`; crypto_alt avg `0.692` n `229`; crypto_major avg `0.7344` n `8`; equity avg `0.546` n `91`; fx avg `0.0115` n `6`; index avg `0.0783` n `25`; metal avg `-0.1463` n `20`; unknown avg `0.1334` n `765`
- 24h: commodity avg `-0.9474` n `12`; crypto_alt avg `1.4099` n `229`; crypto_major avg `1.9589` n `8`; equity avg `1.1092` n `91`; fx avg `-0.1034` n `6`; index avg `0.3159` n `25`; metal avg `0.1875` n `20`; unknown avg `0.0403` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
