# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T01:07:30.246919+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.6766` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.5149` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0271` n `12`; crypto_alt avg `-0.128` n `233`; crypto_major avg `-0.1169` n `8`; equity avg `-0.0275` n `136`; fx avg `0.0066` n `6`; index avg `0.0144` n `27`; metal avg `0.0364` n `20`; unknown avg `0.7464` n `906`
- 1h: commodity avg `0.0399` n `12`; crypto_alt avg `-0.0571` n `233`; crypto_major avg `-0.1365` n `8`; equity avg `0.238` n `136`; fx avg `0.0308` n `6`; index avg `0.0682` n `27`; metal avg `0.0417` n `20`; unknown avg `0.6479` n `900`
- 4h: commodity avg `0.0433` n `12`; crypto_alt avg `-0.9585` n `233`; crypto_major avg `-1.4294` n `8`; equity avg `0.2472` n `136`; fx avg `0.0309` n `6`; index avg `0.0855` n `27`; metal avg `-0.0476` n `20`; unknown avg `2.3764` n `888`
- 24h: commodity avg `-0.1992` n `12`; crypto_alt avg `0.9922` n `233`; crypto_major avg `1.9084` n `8`; equity avg `0.4127` n `136`; fx avg `0.0413` n `6`; index avg `0.0525` n `27`; metal avg `-0.3193` n `20`; unknown avg `6.4826` n `794`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
