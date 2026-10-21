# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-21T08:07:29.652421+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0208` n `13`; crypto_alt avg `-0.1861` n `237`; crypto_major avg `-0.1415` n `8`; equity avg `-0.0491` n `151`; fx avg `0.0042` n `6`; index avg `0.0096` n `26`; metal avg `-0.021` n `20`; unknown avg `0.1526` n `1182`
- 1h: commodity avg `-0.1092` n `13`; crypto_alt avg `0.5408` n `237`; crypto_major avg `0.5618` n `8`; equity avg `0.2238` n `151`; fx avg `0.0121` n `6`; index avg `0.0567` n `26`; metal avg `0.0397` n `20`; unknown avg `2.7998` n `1182`
- 4h: commodity avg `-0.1835` n `13`; crypto_alt avg `0.5633` n `237`; crypto_major avg `0.616` n `8`; equity avg `0.0315` n `151`; fx avg `0.0065` n `6`; index avg `0.028` n `26`; metal avg `-0.0548` n `20`; unknown avg `1.5931` n `1158`
- 24h: commodity avg `-0.251` n `13`; crypto_alt avg `3.7068` n `237`; crypto_major avg `2.7945` n `8`; equity avg `2.8015` n `151`; fx avg `0.0256` n `6`; index avg `0.3929` n `26`; metal avg `-0.1102` n `20`; unknown avg `5293.1833` n `986`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1599`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1475`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
