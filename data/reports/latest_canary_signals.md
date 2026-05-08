# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T02:07:16.574935+00:00`
- Correlation status: `ready`
- Asset price records: `604`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.17` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0577` n `12`; crypto_alt avg `-0.3553` n `228`; crypto_major avg `-0.2111` n `8`; equity avg `-0.1405` n `65`; fx avg `0.0098` n `5`; index avg `0.0024` n `23`; metal avg `0.0935` n `18`; unknown avg `-0.468` n `365`
- 1h: commodity avg `-0.09` n `12`; crypto_alt avg `-0.5384` n `228`; crypto_major avg `-0.3231` n `8`; equity avg `-0.0576` n `65`; fx avg `0.0095` n `5`; index avg `0.0601` n `23`; metal avg `0.1938` n `18`; unknown avg `-0.3661` n `365`
- 4h: commodity avg `-0.4792` n `12`; crypto_alt avg `0.0662` n `228`; crypto_major avg `-0.1863` n `8`; equity avg `0.837` n `65`; fx avg `0.109` n `5`; index avg `0.5062` n `23`; metal avg `1.1873` n `18`; unknown avg `-0.5466` n `365`
- 24h: commodity avg `0.7699` n `12`; crypto_alt avg `1.7161` n `228`; crypto_major avg `-1.4845` n `8`; equity avg `-0.964` n `65`; fx avg `0.2037` n `5`; index avg `-0.5549` n `23`; metal avg `0.179` n `18`; unknown avg `-0.4248` n `355`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1311`, n `600`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1201`, n `600`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1122`, n `600`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1109`, n `600`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1083`, n `596`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1067`, n `596`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0903`, n `596`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0898`, n `596`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0775`, n `596`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0744`, n `600`, weak_sample_signal
