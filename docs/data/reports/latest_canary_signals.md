# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T09:37:25.531663+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.05` n `13`; crypto_alt avg `0.2053` n `239`; crypto_major avg `0.1776` n `8`; equity avg `0.0847` n `158`; fx avg `0.0017` n `6`; index avg `-0.0059` n `27`; metal avg `0.0011` n `20`; unknown avg `0.0409` n `1198`
- 1h: commodity avg `-0.1591` n `13`; crypto_alt avg `-0.1904` n `239`; crypto_major avg `-0.0513` n `8`; equity avg `0.0628` n `158`; fx avg `0.0067` n `6`; index avg `-0.0468` n `27`; metal avg `0.006` n `20`; unknown avg `-0.0577` n `1192`
- 4h: commodity avg `0.0547` n `13`; crypto_alt avg `-0.2073` n `239`; crypto_major avg `-0.0298` n `8`; equity avg `0.1675` n `158`; fx avg `0.0152` n `6`; index avg `-0.0131` n `27`; metal avg `0.0165` n `20`; unknown avg `0.0812` n `1156`
- 24h: commodity avg `0.1471` n `13`; crypto_alt avg `-1.6673` n `239`; crypto_major avg `-0.6098` n `8`; equity avg `0.0009` n `158`; fx avg `0.061` n `6`; index avg `-0.0068` n `27`; metal avg `-0.0188` n `20`; unknown avg `-0.2669` n `1109`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1636`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1576`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
