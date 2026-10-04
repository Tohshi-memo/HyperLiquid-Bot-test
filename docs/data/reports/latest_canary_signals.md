# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T18:22:25.126591+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0118` n `13`; crypto_alt avg `0.0445` n `235`; crypto_major avg `-0.0452` n `8`; equity avg `-0.0136` n `144`; fx avg `-0.0042` n `6`; index avg `-0.0049` n `26`; metal avg `0.0001` n `20`; unknown avg `0.2127` n `1076`
- 1h: commodity avg `0.0068` n `13`; crypto_alt avg `0.168` n `235`; crypto_major avg `0.0413` n `8`; equity avg `0.0122` n `144`; fx avg `-0.0124` n `6`; index avg `0.0047` n `26`; metal avg `0.0059` n `20`; unknown avg `-0.0115` n `1074`
- 4h: commodity avg `-0.0204` n `13`; crypto_alt avg `0.0561` n `235`; crypto_major avg `0.3667` n `8`; equity avg `0.0325` n `144`; fx avg `-0.004` n `6`; index avg `-0.0156` n `26`; metal avg `-0.0005` n `20`; unknown avg `0.0479` n `1068`
- 24h: commodity avg `0.0038` n `13`; crypto_alt avg `1.0034` n `235`; crypto_major avg `0.833` n `8`; equity avg `0.2171` n `144`; fx avg `0.0198` n `6`; index avg `-0.0156` n `26`; metal avg `0.0044` n `20`; unknown avg `-0.0934` n `1017`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2036`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.172`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1522`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
