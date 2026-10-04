# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T19:33:53.764915+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0348` n `13`; crypto_alt avg `0.0916` n `235`; crypto_major avg `0.07` n `8`; equity avg `0.0124` n `144`; fx avg `-0.0017` n `6`; index avg `-0.0046` n `26`; metal avg `0.0041` n `20`; unknown avg `0.0082` n `1078`
- 1h: commodity avg `-0.0415` n `13`; crypto_alt avg `0.2522` n `235`; crypto_major avg `0.1497` n `8`; equity avg `0.0038` n `144`; fx avg `0.0018` n `6`; index avg `-0.0036` n `26`; metal avg `0.0067` n `20`; unknown avg `0.2715` n `1076`
- 4h: commodity avg `-0.0072` n `13`; crypto_alt avg `0.4104` n `235`; crypto_major avg `0.4221` n `8`; equity avg `0.0151` n `144`; fx avg `-0.0254` n `6`; index avg `-0.0022` n `26`; metal avg `0.0133` n `20`; unknown avg `0.4095` n `1068`
- 24h: commodity avg `-0.0222` n `13`; crypto_alt avg `1.2711` n `235`; crypto_major avg `1.1734` n `8`; equity avg `0.1901` n `144`; fx avg `0.0273` n `6`; index avg `-0.0244` n `26`; metal avg `0.0036` n `20`; unknown avg `0.4546` n `1023`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2035`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1808`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1767`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1517`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
