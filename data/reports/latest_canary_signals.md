# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T00:52:21.998185+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.45` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.0839` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0736` n `12`; crypto_alt avg `-0.0511` n `228`; crypto_major avg `-0.1693` n `8`; equity avg `0.1995` n `69`; fx avg `0.0224` n `6`; index avg `-0.0338` n `23`; metal avg `0.1526` n `18`; unknown avg `-0.3484` n `422`
- 1h: commodity avg `-0.1393` n `12`; crypto_alt avg `1.1769` n `228`; crypto_major avg `0.696` n `8`; equity avg `0.363` n `69`; fx avg `0.0506` n `6`; index avg `0.2031` n `23`; metal avg `0.3728` n `18`; unknown avg `-0.0889` n `422`
- 4h: commodity avg `0.3058` n `12`; crypto_alt avg `-0.8919` n `228`; crypto_major avg `-0.8266` n `8`; equity avg `0.0273` n `69`; fx avg `0.0007` n `6`; index avg `0.2573` n `23`; metal avg `0.0683` n `18`; unknown avg `-0.3791` n `422`
- 24h: commodity avg `0.4004` n `12`; crypto_alt avg `-4.0049` n `228`; crypto_major avg `-5.4808` n `8`; equity avg `1.9216` n `69`; fx avg `0.0659` n `6`; index avg `1.4068` n `23`; metal avg `0.5043` n `18`; unknown avg `-0.4933` n `412`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1706`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
