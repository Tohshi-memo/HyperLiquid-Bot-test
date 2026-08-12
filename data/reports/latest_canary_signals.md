# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T14:22:28.556952+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.2` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `-1.6196` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0171` n `12`; crypto_alt avg `-0.1502` n `230`; crypto_major avg `-0.0258` n `8`; equity avg `-0.0091` n `113`; fx avg `-0.0098` n `6`; index avg `-0.0047` n `25`; metal avg `0.0342` n `20`; unknown avg `-0.0311` n `786`
- 1h: commodity avg `0.0323` n `12`; crypto_alt avg `-0.5184` n `230`; crypto_major avg `-0.6898` n `8`; equity avg `-0.0697` n `113`; fx avg `0.0172` n `6`; index avg `-0.0478` n `25`; metal avg `0.0309` n `20`; unknown avg `0.2156` n `786`
- 4h: commodity avg `-0.0174` n `12`; crypto_alt avg `-0.3661` n `230`; crypto_major avg `-0.728` n `8`; equity avg `0.8916` n `113`; fx avg `0.0137` n `6`; index avg `0.1181` n `25`; metal avg `0.0014` n `20`; unknown avg `0.021` n `786`
- 24h: commodity avg `0.1812` n `12`; crypto_alt avg `-1.1852` n `230`; crypto_major avg `0.2168` n `8`; equity avg `2.7413` n `113`; fx avg `0.0387` n `6`; index avg `0.3054` n `25`; metal avg `0.3948` n `20`; unknown avg `-0.1446` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2321`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2058`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2024`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1872`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1679`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1642`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1523`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1299`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
