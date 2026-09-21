# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T12:37:31.100794+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.626` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.5233` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0101` n `12`; crypto_alt avg `0.3115` n `234`; crypto_major avg `0.1591` n `8`; equity avg `0.0031` n `140`; fx avg `0.004` n `6`; index avg `-0.008` n `26`; metal avg `0.0236` n `20`; unknown avg `7.8208` n `944`
- 1h: commodity avg `-0.0076` n `12`; crypto_alt avg `0.3364` n `234`; crypto_major avg `0.2348` n `8`; equity avg `0.1672` n `140`; fx avg `0.0168` n `6`; index avg `0.0143` n `26`; metal avg `0.0861` n `20`; unknown avg `0.6851` n `910`
- 4h: commodity avg `-0.1347` n `12`; crypto_alt avg `1.8898` n `234`; crypto_major avg `1.7639` n `8`; equity avg `0.2406` n `140`; fx avg `0.0515` n `6`; index avg `0.0366` n `26`; metal avg `0.1379` n `20`; unknown avg `0.4583` n `910`
- 24h: commodity avg `-0.81` n `12`; crypto_alt avg `7.5315` n `234`; crypto_major avg `6.2825` n `8`; equity avg `2.0852` n `140`; fx avg `-0.0502` n `6`; index avg `0.3768` n `26`; metal avg `0.1904` n `20`; unknown avg `4.0188` n `733`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1952`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.158`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1479`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
