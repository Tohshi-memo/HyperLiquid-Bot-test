# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T09:52:24.302908+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1454` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0222` n `12`; crypto_alt avg `0.0034` n `230`; crypto_major avg `0.0168` n `8`; equity avg `-0.1572` n `94`; fx avg `0.0019` n `6`; index avg `-0.0388` n `25`; metal avg `0.0088` n `20`; unknown avg `-0.0102` n `768`
- 1h: commodity avg `-0.0095` n `12`; crypto_alt avg `0.0578` n `230`; crypto_major avg `0.0118` n `8`; equity avg `-0.0411` n `94`; fx avg `-0.0176` n `6`; index avg `-0.0182` n `25`; metal avg `0.0218` n `20`; unknown avg `-0.0569` n `762`
- 4h: commodity avg `0.0007` n `12`; crypto_alt avg `-1.0422` n `230`; crypto_major avg `-1.2196` n `8`; equity avg `-0.783` n `94`; fx avg `-0.0748` n `6`; index avg `-0.0742` n `25`; metal avg `-0.0287` n `20`; unknown avg `-0.1036` n `746`
- 24h: commodity avg `-0.1592` n `12`; crypto_alt avg `-0.6864` n `230`; crypto_major avg `-0.7673` n `8`; equity avg `-2.8579` n `93`; fx avg `0.0404` n `6`; index avg `-0.4723` n `25`; metal avg `0.0299` n `20`; unknown avg `-0.0367` n `745`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.156`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
