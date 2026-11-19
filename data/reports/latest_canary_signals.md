# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T03:37:22.683753+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0209` n `13`; crypto_alt avg `0.2909` n `239`; crypto_major avg `0.3031` n `8`; equity avg `0.2909` n `164`; fx avg `-0.0109` n `6`; index avg `0.0385` n `27`; metal avg `0.033` n `20`; unknown avg `1.0904` n `1259`
- 1h: commodity avg `-0.1008` n `13`; crypto_alt avg `0.2387` n `239`; crypto_major avg `0.2577` n `8`; equity avg `0.1171` n `164`; fx avg `-0.014` n `6`; index avg `0.026` n `27`; metal avg `-0.2107` n `20`; unknown avg `0.8167` n `1257`
- 4h: commodity avg `-0.0424` n `13`; crypto_alt avg `0.3054` n `239`; crypto_major avg `-0.0868` n `8`; equity avg `-0.1776` n `164`; fx avg `-0.0638` n `6`; index avg `-0.0276` n `27`; metal avg `-0.3084` n `20`; unknown avg `2.616` n `1251`
- 24h: commodity avg `-0.0247` n `13`; crypto_alt avg `-0.386` n `239`; crypto_major avg `-1.7369` n `8`; equity avg `-0.5728` n `164`; fx avg `-0.1418` n `6`; index avg `0.0258` n `27`; metal avg `-0.8117` n `20`; unknown avg `49.922` n `1121`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1291`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
