# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T21:07:33.503185+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0469` n `12`; crypto_alt avg `-0.4501` n `233`; crypto_major avg `-0.5081` n `8`; equity avg `-0.0276` n `136`; fx avg `-0.0067` n `6`; index avg `0.0108` n `27`; metal avg `0.0172` n `20`; unknown avg `0.744` n `906`
- 1h: commodity avg `0.059` n `12`; crypto_alt avg `0.0904` n `233`; crypto_major avg `-0.0347` n `8`; equity avg `0.231` n `136`; fx avg `-0.0122` n `6`; index avg `0.0464` n `27`; metal avg `0.0827` n `20`; unknown avg `7.7931` n `886`
- 4h: commodity avg `0.045` n `12`; crypto_alt avg `0.5291` n `233`; crypto_major avg `0.9611` n `8`; equity avg `-0.3389` n `136`; fx avg `-0.0049` n `6`; index avg `-0.0646` n `27`; metal avg `-0.1305` n `20`; unknown avg `4.2401` n `874`
- 24h: commodity avg `0.1722` n `12`; crypto_alt avg `0.332` n `233`; crypto_major avg `2.266` n `8`; equity avg `-0.6468` n `136`; fx avg `0.0229` n `6`; index avg `-0.2031` n `27`; metal avg `-0.4084` n `20`; unknown avg `6.6572` n `684`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
