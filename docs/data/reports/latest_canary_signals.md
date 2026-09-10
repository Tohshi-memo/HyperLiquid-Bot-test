# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T21:07:29.534218+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0024` n `12`; crypto_alt avg `-0.0095` n `233`; crypto_major avg `-0.0537` n `8`; equity avg `0.0124` n `136`; fx avg `0.0037` n `6`; index avg `0.0005` n `26`; metal avg `0.0385` n `20`; unknown avg `2.2062` n `794`
- 1h: commodity avg `0.1386` n `12`; crypto_alt avg `0.1436` n `233`; crypto_major avg `0.0346` n `8`; equity avg `0.1459` n `136`; fx avg `-0.0117` n `6`; index avg `0.0076` n `26`; metal avg `0.0393` n `20`; unknown avg `10.4849` n `770`
- 4h: commodity avg `0.404` n `12`; crypto_alt avg `0.2183` n `233`; crypto_major avg `0.3572` n `8`; equity avg `-0.5615` n `136`; fx avg `0.005` n `6`; index avg `-0.0544` n `26`; metal avg `-0.199` n `20`; unknown avg `5.7269` n `749`
- 24h: commodity avg `1.1796` n `12`; crypto_alt avg `-2.9669` n `233`; crypto_major avg `-2.3482` n `8`; equity avg `-2.0814` n `136`; fx avg `0.1133` n `6`; index avg `-0.3288` n `26`; metal avg `-1.2381` n `20`; unknown avg `-1.6591` n `667`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
