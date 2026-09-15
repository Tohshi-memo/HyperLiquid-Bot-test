# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T07:37:27.179320+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0414` n `12`; crypto_alt avg `-0.1561` n `233`; crypto_major avg `-0.1232` n `8`; equity avg `0.0068` n `136`; fx avg `-0.0168` n `6`; index avg `-0.0097` n `27`; metal avg `-0.0097` n `20`; unknown avg `1.822` n `908`
- 1h: commodity avg `0.0331` n `12`; crypto_alt avg `-0.2712` n `233`; crypto_major avg `-0.3368` n `8`; equity avg `0.0098` n `136`; fx avg `0.0237` n `6`; index avg `-0.0262` n `27`; metal avg `-0.0476` n `20`; unknown avg `2.5793` n `904`
- 4h: commodity avg `0.1283` n `12`; crypto_alt avg `-0.6478` n `233`; crypto_major avg `-0.8545` n `8`; equity avg `-0.4912` n `136`; fx avg `0.0718` n `6`; index avg `-0.1297` n `27`; metal avg `-0.1958` n `20`; unknown avg `0.7492` n `868`
- 24h: commodity avg `0.0198` n `12`; crypto_alt avg `-1.4521` n `233`; crypto_major avg `-0.8155` n `8`; equity avg `-0.2186` n `136`; fx avg `0.1777` n `6`; index avg `-0.0797` n `27`; metal avg `-0.2868` n `20`; unknown avg `4.5167` n `820`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
