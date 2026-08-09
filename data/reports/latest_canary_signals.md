# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T14:52:24.736114+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0219` n `12`; crypto_alt avg `0.0883` n `230`; crypto_major avg `0.0286` n `8`; equity avg `0.0079` n `112`; fx avg `-0.0014` n `6`; index avg `-0.0035` n `25`; metal avg `0.002` n `20`; unknown avg `-0.0495` n `785`
- 1h: commodity avg `-0.0015` n `12`; crypto_alt avg `0.1404` n `230`; crypto_major avg `0.1074` n `8`; equity avg `0.0469` n `112`; fx avg `0.0045` n `6`; index avg `-0.0042` n `25`; metal avg `0.0124` n `20`; unknown avg `-0.0305` n `785`
- 4h: commodity avg `-0.1359` n `12`; crypto_alt avg `0.4785` n `230`; crypto_major avg `0.3001` n `8`; equity avg `0.1284` n `112`; fx avg `-0.0043` n `6`; index avg `0.0135` n `25`; metal avg `0.0239` n `20`; unknown avg `-0.0104` n `785`
- 24h: commodity avg `0.1875` n `12`; crypto_alt avg `1.0876` n `230`; crypto_major avg `-0.1999` n `8`; equity avg `0.3815` n `112`; fx avg `-0.0098` n `6`; index avg `0.0222` n `25`; metal avg `0.0574` n `20`; unknown avg `0.3615` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0566`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0551`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0535`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0495`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0491`, n `668`, weak_sample_signal
