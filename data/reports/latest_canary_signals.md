# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T10:07:29.102002+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0166` n `12`; crypto_alt avg `-0.0636` n `228`; crypto_major avg `0.0134` n `8`; equity avg `0.0231` n `88`; fx avg `0.0057` n `6`; index avg `0.006` n `23`; metal avg `0.0016` n `20`; unknown avg `-0.0026` n `765`
- 1h: commodity avg `0.1122` n `12`; crypto_alt avg `-0.0127` n `228`; crypto_major avg `0.0833` n `8`; equity avg `0.0106` n `88`; fx avg `0.0098` n `6`; index avg `0.0037` n `23`; metal avg `0.1059` n `20`; unknown avg `-0.0102` n `765`
- 4h: commodity avg `0.3436` n `12`; crypto_alt avg `-0.5312` n `228`; crypto_major avg `-0.2855` n `8`; equity avg `-0.2999` n `88`; fx avg `0.041` n `6`; index avg `-0.0804` n `23`; metal avg `0.5568` n `20`; unknown avg `-0.3334` n `765`
- 24h: commodity avg `0.0743` n `12`; crypto_alt avg `-0.9852` n `228`; crypto_major avg `0.2345` n `8`; equity avg `1.3307` n `88`; fx avg `0.1283` n `6`; index avg `0.1153` n `23`; metal avg `0.2748` n `20`; unknown avg `9.0749` n `734`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0541`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0541`, n `668`, weak_sample_signal
