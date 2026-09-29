# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T18:07:34.537688+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.6874` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.6314` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.5555` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.1305` n `12`; crypto_alt avg `0.5038` n `234`; crypto_major avg `0.3199` n `8`; equity avg `0.1876` n `142`; fx avg `0.0053` n `6`; index avg `0.0344` n `26`; metal avg `0.1126` n `20`; unknown avg `2.0684` n `960`
- 1h: commodity avg `-0.1909` n `12`; crypto_alt avg `-0.1559` n `234`; crypto_major avg `-0.058` n `8`; equity avg `0.1271` n `142`; fx avg `0.0082` n `6`; index avg `0.0485` n `26`; metal avg `0.1531` n `20`; unknown avg `1.8139` n `960`
- 4h: commodity avg `-0.2472` n `12`; crypto_alt avg `-1.7944` n `234`; crypto_major avg `-1.6472` n `8`; equity avg `-0.0917` n `142`; fx avg `-0.0418` n `6`; index avg `-0.0158` n `26`; metal avg `0.0402` n `20`; unknown avg `221.8825` n `892`
- 24h: commodity avg `-0.5657` n `12`; crypto_alt avg `-0.6776` n `234`; crypto_major avg `-1.3845` n `8`; equity avg `0.2248` n `142`; fx avg `-0.1741` n `6`; index avg `-0.0353` n `26`; metal avg `-0.0939` n `20`; unknown avg `0.8347` n `786`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.192`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1915`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.191`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1586`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1442`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1434`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.139`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1382`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1338`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
