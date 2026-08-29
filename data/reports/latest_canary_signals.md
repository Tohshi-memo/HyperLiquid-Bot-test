# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T22:37:24.603924+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0139` n `12`; crypto_alt avg `0.1047` n `231`; crypto_major avg `0.0942` n `8`; equity avg `0.0278` n `128`; fx avg `-0.0054` n `6`; index avg `0.0076` n `26`; metal avg `-0.0023` n `20`; unknown avg `0.1734` n `789`
- 1h: commodity avg `-0.0186` n `12`; crypto_alt avg `0.0182` n `231`; crypto_major avg `0.042` n `8`; equity avg `0.0176` n `128`; fx avg `-0.0017` n `6`; index avg `0.0002` n `26`; metal avg `-0.0107` n `20`; unknown avg `0.4186` n `774`
- 4h: commodity avg `-0.0304` n `12`; crypto_alt avg `-0.0455` n `231`; crypto_major avg `0.0095` n `8`; equity avg `0.2085` n `128`; fx avg `-0.0162` n `6`; index avg `0.0395` n `26`; metal avg `0.0064` n `20`; unknown avg `0.1385` n `774`
- 24h: commodity avg `-0.0594` n `12`; crypto_alt avg `0.6238` n `231`; crypto_major avg `0.9369` n `8`; equity avg `0.452` n `128`; fx avg `-0.0407` n `6`; index avg `0.0836` n `26`; metal avg `0.1129` n `20`; unknown avg `0.0991` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2041`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.057`, n `668`, weak_sample_signal
