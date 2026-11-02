# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T18:22:32.658170+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1463` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0666` n `13`; crypto_alt avg `-0.2316` n `239`; crypto_major avg `-0.2614` n `8`; equity avg `-0.1931` n `156`; fx avg `-0.0036` n `6`; index avg `-0.019` n `27`; metal avg `-0.0057` n `20`; unknown avg `-0.152` n `1265`
- 1h: commodity avg `-0.1951` n `13`; crypto_alt avg `-0.4617` n `239`; crypto_major avg `-0.348` n `8`; equity avg `-0.5585` n `156`; fx avg `-0.0237` n `6`; index avg `-0.0459` n `27`; metal avg `-0.0348` n `20`; unknown avg `23.547` n `1239`
- 4h: commodity avg `-0.6179` n `13`; crypto_alt avg `-1.3267` n `239`; crypto_major avg `-1.2437` n `8`; equity avg `-1.9585` n `156`; fx avg `0.0048` n `6`; index avg `-0.0974` n `27`; metal avg `0.1661` n `20`; unknown avg `15.2435` n `1229`
- 24h: commodity avg `-1.3471` n `13`; crypto_alt avg `-2.7894` n `238`; crypto_major avg `-1.5177` n `8`; equity avg `-1.4553` n `156`; fx avg `0.2568` n `6`; index avg `0.1648` n `27`; metal avg `0.3447` n `20`; unknown avg `7.5922` n `1055`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1704`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1663`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1594`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1581`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1271`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
