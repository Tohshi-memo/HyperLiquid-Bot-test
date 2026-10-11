# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T04:07:33.577404+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0102` n `13`; crypto_alt avg `-0.1306` n `235`; crypto_major avg `-0.0481` n `8`; equity avg `-0.0215` n `150`; fx avg `0.0` n `6`; index avg `-0.0012` n `26`; metal avg `-0.0037` n `20`; unknown avg `0.0582` n `1109`
- 1h: commodity avg `0.0567` n `13`; crypto_alt avg `-1.1554` n `235`; crypto_major avg `-0.5431` n `8`; equity avg `-0.1291` n `150`; fx avg `0.0043` n `6`; index avg `-0.0213` n `26`; metal avg `-0.0078` n `20`; unknown avg `0.676` n `1109`
- 4h: commodity avg `0.0724` n `13`; crypto_alt avg `-1.1791` n `235`; crypto_major avg `-0.6008` n `8`; equity avg `-0.1415` n `150`; fx avg `0.0007` n `6`; index avg `-0.0226` n `26`; metal avg `0.0008` n `20`; unknown avg `-0.0314` n `1109`
- 24h: commodity avg `0.1711` n `13`; crypto_alt avg `-0.178` n `235`; crypto_major avg `-0.3018` n `8`; equity avg `-0.0997` n `150`; fx avg `-0.013` n `6`; index avg `-0.0376` n `26`; metal avg `-0.0182` n `20`; unknown avg `0.3447` n `942`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1549`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1431`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
