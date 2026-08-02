# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T02:22:32.708684+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.0069` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.2292` n `12`; crypto_alt avg `0.0326` n `230`; crypto_major avg `-0.0155` n `8`; equity avg `0.6` n `102`; fx avg `-0.0006` n `6`; index avg `0.1081` n `25`; metal avg `0.0333` n `20`; unknown avg `0.2777` n `782`
- 1h: commodity avg `-0.6419` n `12`; crypto_alt avg `0.5627` n `230`; crypto_major avg `0.671` n `8`; equity avg `0.8238` n `102`; fx avg `-0.0061` n `6`; index avg `0.1455` n `25`; metal avg `0.0372` n `20`; unknown avg `1.4249` n `782`
- 4h: commodity avg `-0.8673` n `12`; crypto_alt avg `1.0731` n `230`; crypto_major avg `1.1396` n `8`; equity avg `1.0913` n `102`; fx avg `-0.0347` n `6`; index avg `0.2125` n `25`; metal avg `0.0644` n `20`; unknown avg `2.2744` n `782`
- 24h: commodity avg `-0.8889` n `12`; crypto_alt avg `0.0152` n `230`; crypto_major avg `-0.0153` n `8`; equity avg `0.8965` n `102`; fx avg `-0.0796` n `6`; index avg `0.1475` n `25`; metal avg `0.1376` n `20`; unknown avg `0.0636` n `765`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
