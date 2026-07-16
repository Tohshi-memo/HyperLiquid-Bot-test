# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T00:52:24.679207+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0241` n `12`; crypto_alt avg `0.0235` n `230`; crypto_major avg `0.0854` n `8`; equity avg `-0.0267` n `94`; fx avg `-0.0033` n `6`; index avg `-0.0229` n `25`; metal avg `-0.013` n `20`; unknown avg `0.1088` n `768`
- 1h: commodity avg `-0.0393` n `12`; crypto_alt avg `-0.0459` n `230`; crypto_major avg `-0.2383` n `8`; equity avg `-0.324` n `94`; fx avg `-0.0087` n `6`; index avg `-0.1082` n `25`; metal avg `-0.0173` n `20`; unknown avg `-0.0757` n `766`
- 4h: commodity avg `-0.1195` n `12`; crypto_alt avg `-0.2051` n `230`; crypto_major avg `-0.3386` n `8`; equity avg `-0.5152` n `94`; fx avg `-0.0015` n `6`; index avg `-0.1309` n `25`; metal avg `-0.0516` n `20`; unknown avg `0.2113` n `766`
- 24h: commodity avg `-0.1126` n `12`; crypto_alt avg `0.046` n `230`; crypto_major avg `0.1976` n `8`; equity avg `-1.4649` n `93`; fx avg `0.1787` n `6`; index avg `-0.386` n `25`; metal avg `0.027` n `20`; unknown avg `0.0992` n `745`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.158`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
