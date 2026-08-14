# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T15:22:26.214414+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0298` n `12`; crypto_alt avg `-0.0409` n `230`; crypto_major avg `0.0677` n `8`; equity avg `-0.2772` n `114`; fx avg `0.0131` n `6`; index avg `-0.0459` n `25`; metal avg `-0.0578` n `20`; unknown avg `0.061` n `791`
- 1h: commodity avg `0.0546` n `12`; crypto_alt avg `-0.1985` n `230`; crypto_major avg `0.1769` n `8`; equity avg `-0.4705` n `114`; fx avg `0.014` n `6`; index avg `-0.0783` n `25`; metal avg `-0.06` n `20`; unknown avg `0.0282` n `786`
- 4h: commodity avg `0.1514` n `12`; crypto_alt avg `-0.2558` n `230`; crypto_major avg `-0.2288` n `8`; equity avg `-0.8789` n `114`; fx avg `0.0594` n `6`; index avg `-0.1502` n `25`; metal avg `0.1457` n `20`; unknown avg `-0.3434` n `786`
- 24h: commodity avg `0.0096` n `12`; crypto_alt avg `-1.2742` n `230`; crypto_major avg `-1.4062` n `8`; equity avg `-0.7176` n `114`; fx avg `0.0469` n `6`; index avg `-0.115` n `25`; metal avg `0.1167` n `20`; unknown avg `0.2521` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2126`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1785`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1782`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1656`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1563`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1497`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.147`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1466`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1459`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
