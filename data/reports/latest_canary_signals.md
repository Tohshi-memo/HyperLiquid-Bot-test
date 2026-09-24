# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T17:52:36.127132+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0999` n `12`; crypto_alt avg `-0.1585` n `234`; crypto_major avg `-0.1772` n `8`; equity avg `-0.0736` n `141`; fx avg `-0.0102` n `6`; index avg `-0.0237` n `26`; metal avg `-0.0122` n `20`; unknown avg `7.2052` n `943`
- 1h: commodity avg `0.3596` n `12`; crypto_alt avg `-0.3766` n `234`; crypto_major avg `-0.3454` n `8`; equity avg `-0.1982` n `141`; fx avg `0.0073` n `6`; index avg `-0.0866` n `26`; metal avg `-0.114` n `20`; unknown avg `12.1548` n `941`
- 4h: commodity avg `0.859` n `12`; crypto_alt avg `1.8107` n `234`; crypto_major avg `0.9632` n `8`; equity avg `0.599` n `141`; fx avg `0.0024` n `6`; index avg `0.0279` n `26`; metal avg `-0.0203` n `20`; unknown avg `16.7072` n `883`
- 24h: commodity avg `1.2875` n `12`; crypto_alt avg `2.6882` n `234`; crypto_major avg `0.9212` n `8`; equity avg `-0.5948` n `141`; fx avg `0.0275` n `6`; index avg `-0.1334` n `26`; metal avg `-0.1641` n `20`; unknown avg `272.0771` n `833`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.167`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1591`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
