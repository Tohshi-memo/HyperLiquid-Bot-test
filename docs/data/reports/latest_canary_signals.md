# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T17:52:29.827994+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0507` n `12`; crypto_alt avg `-0.0633` n `230`; crypto_major avg `-0.0207` n `8`; equity avg `-0.213` n `96`; fx avg `-0.0101` n `6`; index avg `-0.0561` n `25`; metal avg `-0.0311` n `20`; unknown avg `0.0076` n `769`
- 1h: commodity avg `0.1231` n `12`; crypto_alt avg `0.1251` n `230`; crypto_major avg `0.2715` n `8`; equity avg `0.0817` n `96`; fx avg `-0.0205` n `6`; index avg `-0.0429` n `25`; metal avg `-0.0383` n `20`; unknown avg `0.1353` n `769`
- 4h: commodity avg `0.185` n `12`; crypto_alt avg `1.116` n `230`; crypto_major avg `1.2374` n `8`; equity avg `2.7267` n `96`; fx avg `0.0784` n `6`; index avg `0.3426` n `25`; metal avg `0.2419` n `20`; unknown avg `0.8` n `769`
- 24h: commodity avg `0.9084` n `12`; crypto_alt avg `-0.7943` n `230`; crypto_major avg `-0.8869` n `8`; equity avg `-0.3097` n `94`; fx avg `0.0792` n `6`; index avg `-0.1748` n `25`; metal avg `-0.0731` n `20`; unknown avg `-0.0034` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
