# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T00:37:28.361675+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1196` n `13`; crypto_alt avg `-0.0591` n `236`; crypto_major avg `0.0327` n `8`; equity avg `0.0519` n `151`; fx avg `0.0021` n `6`; index avg `0.0061` n `26`; metal avg `-0.0108` n `20`; unknown avg `0.708` n `1193`
- 1h: commodity avg `0.0458` n `13`; crypto_alt avg `-0.0619` n `236`; crypto_major avg `-0.0925` n `8`; equity avg `0.2453` n `151`; fx avg `0.01` n `6`; index avg `0.0276` n `26`; metal avg `0.0018` n `20`; unknown avg `0.1639` n `1185`
- 4h: commodity avg `0.1072` n `13`; crypto_alt avg `0.336` n `236`; crypto_major avg `0.2582` n `8`; equity avg `-0.187` n `151`; fx avg `0.0108` n `6`; index avg `-0.0182` n `26`; metal avg `-0.0037` n `20`; unknown avg `0.4348` n `1177`
- 24h: commodity avg `0.5009` n `13`; crypto_alt avg `-1.4596` n `236`; crypto_major avg `-1.268` n `8`; equity avg `-3.5227` n `151`; fx avg `-0.0138` n `6`; index avg `-0.569` n `26`; metal avg `0.028` n `20`; unknown avg `40.1594` n `910`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1695`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1175`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1137`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0912`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0772`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
