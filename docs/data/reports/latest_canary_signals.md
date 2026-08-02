# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T01:22:35.403470+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.036` n `12`; crypto_alt avg `0.0535` n `230`; crypto_major avg `0.0471` n `8`; equity avg `-0.0063` n `102`; fx avg `-0.0081` n `6`; index avg `-0.0011` n `25`; metal avg `-0.0025` n `20`; unknown avg `0.1257` n `782`
- 1h: commodity avg `-0.1322` n `12`; crypto_alt avg `0.2795` n `230`; crypto_major avg `0.2759` n `8`; equity avg `0.0047` n `102`; fx avg `0.0169` n `6`; index avg `0.0082` n `25`; metal avg `0.0427` n `20`; unknown avg `2.6825` n `782`
- 4h: commodity avg `-0.3787` n `12`; crypto_alt avg `0.5889` n `230`; crypto_major avg `0.5847` n `8`; equity avg `0.4832` n `102`; fx avg `-0.0122` n `6`; index avg `0.0741` n `25`; metal avg `0.0533` n `20`; unknown avg `0.7459` n `782`
- 24h: commodity avg `-0.2626` n `12`; crypto_alt avg `-0.4376` n `230`; crypto_major avg `-0.5532` n `8`; equity avg `0.1286` n `102`; fx avg `-0.0406` n `6`; index avg `0.0532` n `25`; metal avg `0.1057` n `20`; unknown avg `-0.0246` n `765`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
