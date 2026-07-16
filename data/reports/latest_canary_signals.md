# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T01:52:33.906243+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.02` n `12`; crypto_alt avg `0.2519` n `230`; crypto_major avg `0.1861` n `8`; equity avg `0.2248` n `94`; fx avg `0.0067` n `6`; index avg `0.0446` n `25`; metal avg `-0.0158` n `20`; unknown avg `-0.0194` n `768`
- 1h: commodity avg `0.0198` n `12`; crypto_alt avg `0.2012` n `230`; crypto_major avg `0.1658` n `8`; equity avg `0.004` n `94`; fx avg `0.0139` n `6`; index avg `-0.02` n `25`; metal avg `-0.1662` n `20`; unknown avg `-0.1724` n `768`
- 4h: commodity avg `-0.0864` n `12`; crypto_alt avg `0.0335` n `230`; crypto_major avg `-0.1354` n `8`; equity avg `-0.4564` n `94`; fx avg `-0.0032` n `6`; index avg `-0.1367` n `25`; metal avg `-0.2056` n `20`; unknown avg `-0.0681` n `766`
- 24h: commodity avg `-0.0361` n `12`; crypto_alt avg `0.2835` n `230`; crypto_major avg `0.8202` n `8`; equity avg `-1.6006` n `93`; fx avg `0.1719` n `6`; index avg `-0.3554` n `25`; metal avg `-0.0246` n `20`; unknown avg `0.0749` n `745`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1558`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
