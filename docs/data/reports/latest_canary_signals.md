# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T09:52:25.775935+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.031` n `13`; crypto_alt avg `0.3412` n `235`; crypto_major avg `0.0761` n `8`; equity avg `0.0034` n `143`; fx avg `-0.003` n `6`; index avg `-0.0024` n `26`; metal avg `-0.0032` n `20`; unknown avg `0.0308` n `984`
- 1h: commodity avg `0.0285` n `13`; crypto_alt avg `0.3508` n `235`; crypto_major avg `0.0989` n `8`; equity avg `-0.0003` n `143`; fx avg `-0.0135` n `6`; index avg `-0.0014` n `26`; metal avg `-0.0018` n `20`; unknown avg `1.0299` n `982`
- 4h: commodity avg `0.0746` n `13`; crypto_alt avg `-0.3148` n `235`; crypto_major avg `-0.0879` n `8`; equity avg `0.0093` n `143`; fx avg `0.0019` n `6`; index avg `-0.0135` n `26`; metal avg `0.0039` n `20`; unknown avg `0.3183` n `944`
- 24h: commodity avg `0.7529` n `13`; crypto_alt avg `-2.2322` n `235`; crypto_major avg `-2.3082` n `8`; equity avg `-0.0457` n `142`; fx avg `0.0182` n `6`; index avg `0.1141` n `26`; metal avg `-0.307` n `20`; unknown avg `-0.3978` n `872`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1854`, n `669`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1741`, n `669`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1478`, n `669`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1443`, n `669`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1136`, n `669`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1131`, n `669`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1117`, n `669`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1093`, n `669`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1069`, n `669`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0887`, n `669`, weak_sample_signal
