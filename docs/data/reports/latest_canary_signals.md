# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T13:07:34.331335+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0108` n `12`; crypto_alt avg `-0.1087` n `228`; crypto_major avg `-0.0852` n `8`; equity avg `-0.1624` n `74`; fx avg `0.0045` n `6`; index avg `-0.0473` n `23`; metal avg `0.0251` n `18`; unknown avg `-0.0862` n `643`
- 1h: commodity avg `0.344` n `12`; crypto_alt avg `-0.0585` n `228`; crypto_major avg `0.0787` n `8`; equity avg `-0.6429` n `74`; fx avg `-0.0095` n `6`; index avg `-0.2428` n `23`; metal avg `-0.3858` n `18`; unknown avg `0.097` n `643`
- 4h: commodity avg `0.9751` n `12`; crypto_alt avg `0.247` n `228`; crypto_major avg `0.3705` n `8`; equity avg `-0.4287` n `74`; fx avg `0.0053` n `6`; index avg `-0.0441` n `23`; metal avg `-0.5424` n `18`; unknown avg `1.6903` n `643`
- 24h: commodity avg `-2.437` n `12`; crypto_alt avg `2.2041` n `228`; crypto_major avg `2.2141` n `8`; equity avg `2.5504` n `74`; fx avg `-0.0063` n `6`; index avg `1.5157` n `23`; metal avg `2.8522` n `18`; unknown avg `1.686` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
