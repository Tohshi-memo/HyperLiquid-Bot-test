# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T21:18:32.339608+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1839` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0349` n `12`; crypto_alt avg `-0.3976` n `232`; crypto_major avg `-0.4525` n `8`; equity avg `-0.1042` n `131`; fx avg `0.0139` n `6`; index avg `-0.0061` n `26`; metal avg `-0.0021` n `20`; unknown avg `-0.1429` n `787`
- 1h: commodity avg `-0.0501` n `12`; crypto_alt avg `-0.619` n `232`; crypto_major avg `-0.678` n `8`; equity avg `-0.1581` n `131`; fx avg `0.0083` n `6`; index avg `0.0071` n `26`; metal avg `0.0256` n `20`; unknown avg `-0.0994` n `773`
- 4h: commodity avg `0.246` n `12`; crypto_alt avg `-0.859` n `232`; crypto_major avg `-1.2028` n `8`; equity avg `-0.1616` n `131`; fx avg `0.0126` n `6`; index avg `-0.0189` n `26`; metal avg `-0.1811` n `20`; unknown avg `1.6358` n `773`
- 24h: commodity avg `0.8085` n `12`; crypto_alt avg `-0.6896` n `232`; crypto_major avg `-2.4644` n `8`; equity avg `-1.9689` n `130`; fx avg `0.0504` n `6`; index avg `-0.3407` n `26`; metal avg `-0.8629` n `20`; unknown avg `-0.4296` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0472`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0443`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0377`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0336`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.032`, n `668`, weak_sample_signal
