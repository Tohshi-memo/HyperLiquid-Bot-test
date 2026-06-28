# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T12:22:28.234072+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0217` n `12`; crypto_alt avg `-0.1809` n `228`; crypto_major avg `-0.2509` n `8`; equity avg `-0.0199` n `88`; fx avg `-0.001` n `6`; index avg `-0.0015` n `23`; metal avg `0.0067` n `20`; unknown avg `-0.0286` n `764`
- 1h: commodity avg `0.0377` n `12`; crypto_alt avg `-0.0662` n `228`; crypto_major avg `-0.2166` n `8`; equity avg `-0.0698` n `88`; fx avg `0.0107` n `6`; index avg `-0.0066` n `23`; metal avg `-0.0018` n `20`; unknown avg `0.1104` n `764`
- 4h: commodity avg `-0.0002` n `12`; crypto_alt avg `0.2189` n `228`; crypto_major avg `0.1848` n `8`; equity avg `0.0675` n `88`; fx avg `0.0245` n `6`; index avg `0.0232` n `23`; metal avg `0.0159` n `20`; unknown avg `-1.1009` n `750`
- 24h: commodity avg `0.1404` n `12`; crypto_alt avg `-0.1868` n `228`; crypto_major avg `-0.6632` n `8`; equity avg `0.0771` n `88`; fx avg `0.0014` n `6`; index avg `-0.0494` n `23`; metal avg `-0.014` n `20`; unknown avg `15.617` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2079`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1868`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
