# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T09:07:28.841417+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.047` n `13`; crypto_alt avg `-0.0503` n `239`; crypto_major avg `-0.1522` n `8`; equity avg `0.191` n `162`; fx avg `-0.0118` n `6`; index avg `0.0311` n `27`; metal avg `0.0653` n `20`; unknown avg `-0.0608` n `1256`
- 1h: commodity avg `0.0001` n `13`; crypto_alt avg `-0.2498` n `239`; crypto_major avg `-0.0432` n `8`; equity avg `-0.0819` n `162`; fx avg `-0.0059` n `6`; index avg `-0.0078` n `27`; metal avg `0.0334` n `20`; unknown avg `0.0041` n `1244`
- 4h: commodity avg `0.1072` n `13`; crypto_alt avg `2.1944` n `239`; crypto_major avg `1.283` n `8`; equity avg `-0.1044` n `162`; fx avg `0.0556` n `6`; index avg `-0.0206` n `27`; metal avg `-0.1669` n `20`; unknown avg `0.4963` n `1168`
- 24h: commodity avg `0.5672` n `13`; crypto_alt avg `-0.8094` n `239`; crypto_major avg `-3.1082` n `8`; equity avg `-1.2069` n `162`; fx avg `-0.029` n `6`; index avg `0.0196` n `27`; metal avg `-0.3385` n `20`; unknown avg `102.9442` n `1093`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
