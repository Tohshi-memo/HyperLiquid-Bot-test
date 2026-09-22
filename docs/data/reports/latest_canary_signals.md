# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T10:22:35.559524+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0445` n `12`; crypto_alt avg `-0.153` n `234`; crypto_major avg `-0.0607` n `8`; equity avg `-0.106` n `140`; fx avg `0.0173` n `6`; index avg `-0.0304` n `26`; metal avg `-0.0159` n `20`; unknown avg `-0.1131` n `942`
- 1h: commodity avg `-0.291` n `12`; crypto_alt avg `-0.2742` n `234`; crypto_major avg `-0.0086` n `8`; equity avg `0.3628` n `140`; fx avg `-0.0133` n `6`; index avg `0.0578` n `26`; metal avg `0.0607` n `20`; unknown avg `6.6392` n `940`
- 4h: commodity avg `-0.6767` n `12`; crypto_alt avg `0.0299` n `234`; crypto_major avg `0.4275` n `8`; equity avg `0.4749` n `140`; fx avg `-0.0902` n `6`; index avg `0.0516` n `26`; metal avg `0.0996` n `20`; unknown avg `6.5484` n `934`
- 24h: commodity avg `-0.6146` n `12`; crypto_alt avg `0.5843` n `234`; crypto_major avg `1.696` n `8`; equity avg `0.9882` n `140`; fx avg `-0.2613` n `6`; index avg `0.2718` n `26`; metal avg `-0.1316` n `20`; unknown avg `1133.3298` n `790`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1355`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
