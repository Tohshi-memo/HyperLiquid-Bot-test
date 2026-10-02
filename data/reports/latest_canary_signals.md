# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T16:22:32.372133+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.7503` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.4554` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0329` n `13`; crypto_alt avg `0.0716` n `235`; crypto_major avg `0.028` n `8`; equity avg `0.0132` n `143`; fx avg `-0.0062` n `6`; index avg `-0.0033` n `26`; metal avg `0.0537` n `20`; unknown avg `-0.0583` n `984`
- 1h: commodity avg `0.1637` n `13`; crypto_alt avg `0.3891` n `235`; crypto_major avg `0.0491` n `8`; equity avg `0.1839` n `143`; fx avg `-0.014` n `6`; index avg `0.0464` n `26`; metal avg `-0.0476` n `20`; unknown avg `8.3861` n `976`
- 4h: commodity avg `0.3261` n `13`; crypto_alt avg `-0.1459` n `235`; crypto_major avg `-1.3399` n `8`; equity avg `0.4104` n `142`; fx avg `0.0494` n `6`; index avg `0.1155` n `26`; metal avg `-0.3103` n `20`; unknown avg `1.2127` n `934`
- 24h: commodity avg `-0.154` n `13`; crypto_alt avg `2.703` n `235`; crypto_major avg `1.3183` n `8`; equity avg `1.8229` n `142`; fx avg `-0.1463` n `6`; index avg `0.4921` n `26`; metal avg `-0.2154` n `20`; unknown avg `101.4837` n `824`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1692`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1648`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
