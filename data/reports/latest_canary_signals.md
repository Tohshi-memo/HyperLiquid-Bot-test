# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T11:22:26.960452+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.78` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0229` n `12`; crypto_alt avg `-0.1294` n `228`; crypto_major avg `-0.1197` n `8`; equity avg `0.1812` n `69`; fx avg `-0.0` n `6`; index avg `0.021` n `23`; metal avg `-0.0176` n `18`; unknown avg `-0.0878` n `422`
- 1h: commodity avg `-0.1364` n `12`; crypto_alt avg `0.1791` n `228`; crypto_major avg `0.0794` n `8`; equity avg `-0.0693` n `69`; fx avg `0.0204` n `6`; index avg `-0.1038` n `23`; metal avg `0.0468` n `18`; unknown avg `0.7894` n `422`
- 4h: commodity avg `-0.0134` n `12`; crypto_alt avg `0.1132` n `228`; crypto_major avg `-0.4976` n `8`; equity avg `0.1389` n `69`; fx avg `0.0025` n `6`; index avg `0.0772` n `23`; metal avg `-0.4047` n `18`; unknown avg `-0.1649` n `422`
- 24h: commodity avg `-0.8161` n `12`; crypto_alt avg `-0.1994` n `228`; crypto_major avg `-2.1149` n `8`; equity avg `0.7275` n `69`; fx avg `0.1411` n `6`; index avg `0.0224` n `23`; metal avg `0.6388` n `18`; unknown avg `1.0788` n `408`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1653`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
