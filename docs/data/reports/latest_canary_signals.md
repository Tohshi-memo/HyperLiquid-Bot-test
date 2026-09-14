# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T21:52:26.349817+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.0324` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0147` n `12`; crypto_alt avg `-0.0359` n `233`; crypto_major avg `-0.0292` n `8`; equity avg `-0.0015` n `136`; fx avg `0.004` n `6`; index avg `0.0115` n `27`; metal avg `-0.007` n `20`; unknown avg `0.0352` n `908`
- 1h: commodity avg `0.0364` n `12`; crypto_alt avg `-0.9472` n `233`; crypto_major avg `-1.0244` n `8`; equity avg `-0.0624` n `136`; fx avg `0.008` n `6`; index avg `0.008` n `27`; metal avg `0.0207` n `20`; unknown avg `1.527` n `906`
- 4h: commodity avg `0.0256` n `12`; crypto_alt avg `-0.3342` n `233`; crypto_major avg `-0.0081` n `8`; equity avg `-0.5874` n `136`; fx avg `0.0081` n `6`; index avg `-0.0951` n `27`; metal avg `-0.099` n `20`; unknown avg `4.8503` n `874`
- 24h: commodity avg `0.3426` n `12`; crypto_alt avg `0.0097` n `233`; crypto_major avg `1.8614` n `8`; equity avg `-0.7682` n `136`; fx avg `0.0352` n `6`; index avg `-0.2323` n `27`; metal avg `-0.4138` n `20`; unknown avg `6.0599` n `684`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
