# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T09:07:27.772651+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0459` n `13`; crypto_alt avg `-0.0402` n `236`; crypto_major avg `-0.0615` n `8`; equity avg `-0.128` n `151`; fx avg `0.0108` n `6`; index avg `-0.0163` n `26`; metal avg `0.026` n `20`; unknown avg `-0.1676` n `1134`
- 1h: commodity avg `-0.0864` n `13`; crypto_alt avg `0.2076` n `236`; crypto_major avg `0.1558` n `8`; equity avg `-0.0534` n `151`; fx avg `0.028` n `6`; index avg `-0.0021` n `26`; metal avg `0.0581` n `20`; unknown avg `-0.1385` n `1110`
- 4h: commodity avg `-0.0369` n `13`; crypto_alt avg `0.2992` n `236`; crypto_major avg `0.1902` n `8`; equity avg `-0.6411` n `151`; fx avg `-0.0476` n `6`; index avg `-0.097` n `26`; metal avg `0.0584` n `20`; unknown avg `0.0423` n `1048`
- 24h: commodity avg `-0.1146` n `13`; crypto_alt avg `3.8365` n `236`; crypto_major avg `1.933` n `8`; equity avg `2.3192` n `151`; fx avg `0.0048` n `6`; index avg `0.303` n `26`; metal avg `0.3821` n `20`; unknown avg `27.0986` n `864`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.0968`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0937`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0915`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0881`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.075`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
