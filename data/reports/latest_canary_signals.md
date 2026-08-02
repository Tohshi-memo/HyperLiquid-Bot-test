# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T05:52:29.556017+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0136` n `12`; crypto_alt avg `0.0911` n `230`; crypto_major avg `0.0461` n `8`; equity avg `-0.0039` n `102`; fx avg `0.0013` n `6`; index avg `-0.003` n `25`; metal avg `-0.0086` n `20`; unknown avg `1.4228` n `782`
- 1h: commodity avg `0.0258` n `12`; crypto_alt avg `0.1407` n `230`; crypto_major avg `0.0348` n `8`; equity avg `-0.074` n `102`; fx avg `-0.0225` n `6`; index avg `0.0115` n `25`; metal avg `0.0069` n `20`; unknown avg `0.2593` n `782`
- 4h: commodity avg `-0.7878` n `12`; crypto_alt avg `0.7389` n `230`; crypto_major avg `0.9111` n `8`; equity avg `0.7357` n `102`; fx avg `-0.057` n `6`; index avg `0.1895` n `25`; metal avg `0.1573` n `20`; unknown avg `0.7065` n `782`
- 24h: commodity avg `-1.0411` n `12`; crypto_alt avg `0.4414` n `230`; crypto_major avg `0.6743` n `8`; equity avg `0.8403` n `102`; fx avg `-0.1189` n `6`; index avg `0.254` n `25`; metal avg `0.2601` n `20`; unknown avg `0.3849` n `765`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
