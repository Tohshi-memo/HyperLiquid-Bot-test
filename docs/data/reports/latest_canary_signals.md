# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T18:52:25.354512+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0156` n `13`; crypto_alt avg `0.0272` n `239`; crypto_major avg `0.0063` n `8`; equity avg `-0.018` n `158`; fx avg `0.0081` n `6`; index avg `-0.0028` n `27`; metal avg `0.0033` n `20`; unknown avg `0.1675` n `1262`
- 1h: commodity avg `-0.013` n `13`; crypto_alt avg `0.0382` n `239`; crypto_major avg `0.097` n `8`; equity avg `0.0722` n `158`; fx avg `0.0086` n `6`; index avg `-0.0049` n `27`; metal avg `0.0108` n `20`; unknown avg `0.2763` n `1240`
- 4h: commodity avg `0.033` n `13`; crypto_alt avg `-0.1098` n `239`; crypto_major avg `-0.1576` n `8`; equity avg `0.0538` n `158`; fx avg `0.0022` n `6`; index avg `0.028` n `27`; metal avg `-0.0186` n `20`; unknown avg `165.5489` n `1209`
- 24h: commodity avg `0.1357` n `13`; crypto_alt avg `-1.2709` n `239`; crypto_major avg `-0.5561` n `8`; equity avg `0.3485` n `158`; fx avg `-0.0011` n `6`; index avg `0.0277` n `27`; metal avg `-0.0646` n `20`; unknown avg `0.1743` n `1077`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1643`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
