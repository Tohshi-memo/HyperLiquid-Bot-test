# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T13:07:27.544284+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0515` n `12`; crypto_alt avg `0.1716` n `231`; crypto_major avg `0.1443` n `8`; equity avg `0.0956` n `127`; fx avg `0.0175` n `6`; index avg `0.017` n `26`; metal avg `0.0323` n `20`; unknown avg `-0.0119` n `792`
- 1h: commodity avg `-0.0138` n `12`; crypto_alt avg `0.1852` n `231`; crypto_major avg `0.0294` n `8`; equity avg `-0.0367` n `127`; fx avg `0.0227` n `6`; index avg `-0.0138` n `26`; metal avg `-0.0808` n `20`; unknown avg `-0.0559` n `792`
- 4h: commodity avg `0.1508` n `12`; crypto_alt avg `-0.6207` n `231`; crypto_major avg `-0.5615` n `8`; equity avg `-0.3133` n `127`; fx avg `0.0247` n `6`; index avg `-0.0177` n `26`; metal avg `-0.0462` n `20`; unknown avg `0.0425` n `792`
- 24h: commodity avg `0.4131` n `12`; crypto_alt avg `1.5939` n `231`; crypto_major avg `2.2263` n `8`; equity avg `2.2516` n `127`; fx avg `-0.0611` n `6`; index avg `0.3319` n `26`; metal avg `-0.3313` n `20`; unknown avg `0.4659` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
