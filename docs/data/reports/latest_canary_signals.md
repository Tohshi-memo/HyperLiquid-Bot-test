# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T02:37:26.027431+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0005` n `12`; crypto_alt avg `0.0232` n `234`; crypto_major avg `-0.0002` n `8`; equity avg `-0.0453` n `140`; fx avg `0.0037` n `6`; index avg `-0.0026` n `26`; metal avg `-0.0131` n `20`; unknown avg `0.7422` n `945`
- 1h: commodity avg `-0.0637` n `12`; crypto_alt avg `0.01` n `234`; crypto_major avg `0.1324` n `8`; equity avg `-0.2323` n `140`; fx avg `0.0376` n `6`; index avg `-0.0274` n `26`; metal avg `-0.1234` n `20`; unknown avg `0.606` n `943`
- 4h: commodity avg `0.0241` n `12`; crypto_alt avg `0.5532` n `234`; crypto_major avg `0.4849` n `8`; equity avg `-0.4267` n `140`; fx avg `-0.0644` n `6`; index avg `-0.1126` n `26`; metal avg `-0.2716` n `20`; unknown avg `1.1986` n `937`
- 24h: commodity avg `-0.0027` n `12`; crypto_alt avg `2.5809` n `234`; crypto_major avg `1.4568` n `8`; equity avg `0.2045` n `140`; fx avg `-0.1945` n `6`; index avg `-0.007` n `26`; metal avg `-0.0026` n `20`; unknown avg `0.9887` n `836`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1454`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1421`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
