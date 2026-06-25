# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T20:52:30.307058+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0528` n `12`; crypto_alt avg `-0.3225` n `228`; crypto_major avg `-0.3967` n `8`; equity avg `-0.0781` n `86`; fx avg `-0.0043` n `6`; index avg `-0.024` n `23`; metal avg `-0.0347` n `20`; unknown avg `0.1374` n `765`
- 1h: commodity avg `-0.0823` n `12`; crypto_alt avg `0.411` n `228`; crypto_major avg `0.2325` n `8`; equity avg `0.2876` n `86`; fx avg `0.002` n `6`; index avg `0.0433` n `23`; metal avg `-0.0055` n `20`; unknown avg `0.1229` n `765`
- 4h: commodity avg `-0.0382` n `12`; crypto_alt avg `0.3047` n `228`; crypto_major avg `0.5471` n `8`; equity avg `0.2184` n `86`; fx avg `0.0105` n `6`; index avg `0.0204` n `23`; metal avg `-0.1524` n `20`; unknown avg `0.2913` n `765`
- 24h: commodity avg `0.3857` n `12`; crypto_alt avg `-1.8139` n `228`; crypto_major avg `-2.0884` n `8`; equity avg `-2.0599` n `86`; fx avg `0.0855` n `6`; index avg `-0.1251` n `23`; metal avg `0.2988` n `20`; unknown avg `0.3884` n `700`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0571`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.057`, n `668`, weak_sample_signal
