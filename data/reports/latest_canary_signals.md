# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T18:22:25.793528+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.016` n `12`; crypto_alt avg `-0.2709` n `232`; crypto_major avg `-0.1155` n `8`; equity avg `-0.0166` n `134`; fx avg `-0.0054` n `6`; index avg `-0.0046` n `26`; metal avg `-0.0119` n `20`; unknown avg `1.3592` n `796`
- 1h: commodity avg `0.0347` n `12`; crypto_alt avg `-0.2601` n `232`; crypto_major avg `-0.1192` n `8`; equity avg `0.0592` n `134`; fx avg `-0.0098` n `6`; index avg `-0.0034` n `26`; metal avg `-0.0285` n `20`; unknown avg `1.1979` n `774`
- 4h: commodity avg `-0.0043` n `12`; crypto_alt avg `-0.828` n `232`; crypto_major avg `-0.4885` n `8`; equity avg `0.162` n `134`; fx avg `-0.024` n `6`; index avg `0.0451` n `26`; metal avg `0.0208` n `20`; unknown avg `0.0439` n `768`
- 24h: commodity avg `0.1764` n `12`; crypto_alt avg `0.0723` n `232`; crypto_major avg `-1.0272` n `8`; equity avg `0.4779` n `134`; fx avg `-0.1245` n `6`; index avg `0.0771` n `26`; metal avg `-0.0241` n `20`; unknown avg `2.0997` n `661`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
