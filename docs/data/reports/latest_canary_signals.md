# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T00:22:25.757457+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0149` n `12`; crypto_alt avg `0.3965` n `231`; crypto_major avg `0.22` n `8`; equity avg `0.1855` n `127`; fx avg `-0.0043` n `6`; index avg `0.0174` n `26`; metal avg `-0.0236` n `20`; unknown avg `0.2507` n `792`
- 1h: commodity avg `-0.0193` n `12`; crypto_alt avg `0.0569` n `231`; crypto_major avg `-0.2545` n `8`; equity avg `0.1081` n `127`; fx avg `-0.0104` n `6`; index avg `0.0215` n `26`; metal avg `-0.0436` n `20`; unknown avg `0.2565` n `792`
- 4h: commodity avg `-0.0122` n `12`; crypto_alt avg `0.268` n `231`; crypto_major avg `-0.1042` n `8`; equity avg `-0.2889` n `127`; fx avg `-0.0094` n `6`; index avg `0.002` n `26`; metal avg `-0.0646` n `20`; unknown avg `0.099` n `792`
- 24h: commodity avg `0.359` n `12`; crypto_alt avg `1.1715` n `231`; crypto_major avg `2.2641` n `8`; equity avg `-0.1265` n `127`; fx avg `0.0075` n `6`; index avg `-0.0485` n `26`; metal avg `0.0091` n `20`; unknown avg `1.1611` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1334`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
