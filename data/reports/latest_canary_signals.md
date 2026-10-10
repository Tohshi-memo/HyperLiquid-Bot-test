# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T17:22:23.958303+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0453` n `13`; crypto_alt avg `0.0729` n `235`; crypto_major avg `0.0407` n `8`; equity avg `0.0021` n `150`; fx avg `-0.0057` n `6`; index avg `0.0008` n `26`; metal avg `-0.0024` n `20`; unknown avg `2.3681` n `1117`
- 1h: commodity avg `0.0896` n `13`; crypto_alt avg `-0.0198` n `235`; crypto_major avg `-0.0862` n `8`; equity avg `-0.0376` n `150`; fx avg `-0.005` n `6`; index avg `-0.0143` n `26`; metal avg `-0.0041` n `20`; unknown avg `2.3428` n `1107`
- 4h: commodity avg `0.0142` n `13`; crypto_alt avg `0.8489` n `235`; crypto_major avg `0.3134` n `8`; equity avg `0.0652` n `150`; fx avg `-0.0125` n `6`; index avg `0.0116` n `26`; metal avg `-0.0151` n `20`; unknown avg `3.344` n `1093`
- 24h: commodity avg `-0.3384` n `13`; crypto_alt avg `2.7162` n `235`; crypto_major avg `1.0051` n `8`; equity avg `0.2803` n `150`; fx avg `-0.0037` n `6`; index avg `0.0467` n `26`; metal avg `0.0006` n `20`; unknown avg `4.1577` n `984`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1565`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
