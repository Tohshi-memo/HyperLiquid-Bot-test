# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T05:01:37.339889+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0234` n `12`; crypto_alt avg `-0.4848` n `228`; crypto_major avg `-0.3347` n `8`; equity avg `-0.0766` n `73`; fx avg `0.0026` n `6`; index avg `-0.0467` n `23`; metal avg `-0.0181` n `18`; unknown avg `0.6874` n `420`
- 1h: commodity avg `0.0136` n `12`; crypto_alt avg `-1.4901` n `228`; crypto_major avg `-0.8543` n `8`; equity avg `-0.0822` n `73`; fx avg `0.0006` n `6`; index avg `0.0551` n `23`; metal avg `0.2348` n `18`; unknown avg `-0.7939` n `420`
- 4h: commodity avg `-0.1667` n `12`; crypto_alt avg `-2.6351` n `228`; crypto_major avg `-0.1972` n `8`; equity avg `0.0526` n `73`; fx avg `0.0183` n `6`; index avg `-0.0004` n `23`; metal avg `0.2738` n `18`; unknown avg `-0.4161` n `420`
- 24h: commodity avg `0.014` n `12`; crypto_alt avg `-3.7561` n `228`; crypto_major avg `-2.9625` n `8`; equity avg `-3.5899` n `73`; fx avg `0.0113` n `6`; index avg `-1.0553` n `23`; metal avg `-1.1981` n `18`; unknown avg `0.9609` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1923`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1728`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1559`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1542`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
